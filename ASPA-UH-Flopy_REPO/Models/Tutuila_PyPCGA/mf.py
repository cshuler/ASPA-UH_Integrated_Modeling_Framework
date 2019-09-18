import flopy
import flopy.utils.binaryfile as bf
import numpy as np
import os
from shutil import copy2, rmtree
from multiprocessing import Pool

class Model:
    def __init__(self, params=None):
        self.idx = 0
        self.homedir = os.path.abspath('./')
        self.deletedir = True

        from psutil import cpu_count  # physcial cpu counts
        self.ncores = cpu_count(logical=False)

        if params is not None:
            if 'deletedir' in params:
                self.deletedir = params['deletedir']
            if 'homedir' in params:
                self.homedir = params['homedir']
            if 'ncores' in params:
                self.ncores = params['ncores']

            self.delr = params['delr']
            self.delc = params['delc']
            self.nlay = params['nlay']
            self.nrow = params['nrow']
            self.ncol = params['ncol']
            self.botm = params['botm']
            self.obs_locmat = params['obs_locmat']
            self.nobs = params['nobs']
            self.layervals = params['layervals']
            self.rowvals = params['rowvals']
            self.colvals = params['colvals']
            self.obsvals = params['obsvals']
            self.obsnames = params['obsnames']
            self.sim_dir = './simul' if 'sim_dir' not in params else params['sim_dir']

        else:
            raise ValueError("You have to provide relevant MODFLOW-FloPy parameters")


    def create_dir(self, idx=None):

        if idx is None:
            idx = self.idx

        mydir = os.path.join(self.sim_dir, "simul{0:04d}".format(idx))
        mydir = os.path.abspath(os.path.join(self.homedir, mydir))

        if not os.path.exists(mydir):
            os.makedirs(mydir)

        #copy2(os.path.abspath(os.path.join(self.homedir,self.input_dir,self.mf_exec)), mydir)

        return mydir

    def run_model_single(self, logHK, idx = 0):
        '''run modflow
        '''
        
        mydir = self.create_dir(idx)
        while not os.path.exists(mydir): # for windows..
            mydir = self.create_dir(idx)
        #self.create_dir(idx)

        laytyp = 0
        vka = 10
        xll = 515244
        yll = 8410178
		
        HK = (np.exp(logHK)).reshape(self.nlay,self.nrow,self.ncol)
		
        exe_name = 'mf2005'

        txtspace = os.path.join('Txt_inputs') 

        # model run times and stress period data
        Number_of_years = 100                           # number of years to run the model,
        nper = 1                                        # Number of model stress periods default is 1
        perlen = [365.25*Number_of_years]               # array of the stress period lengths in days separated by commas
        nstp = [Number_of_years]                        # Number of time steps in each stress period (default is 1 per year).           
        tsmult = 1                                      # Time step multiplier, can be 
        steady = True

        # output control parameters
        Save_every_how_many_steps = 20                  # essentially used for 
        spd = {}
        for istp in range(Save_every_how_many_steps-1, nstp[0]+1, Save_every_how_many_steps):   # format the above for modflow 
            spd[(0, istp)] = ['save head', 'print budget']
            spd[(0, istp+1)] = []

        # load  arrays
        top = np.loadtxt(os.path.join(txtspace, "top.txt"))
        final_ibound = np.loadtxt(os.path.join(txtspace,  "final_ibound.txt"))
        ihead = np.loadtxt(os.path.join(txtspace,  "ihead.txt"))
        
        recharge_converted = np.loadtxt(os.path.join(txtspace,  "recharge_converted.txt"))   
        ghb_geometry = np.loadtxt(os.path.join(txtspace, "ghb_geometry.txt"))   
        # fix some inputs
        rch_data = {0: recharge_converted}   # dictionary form to specify that it is only on first layer    

        ### GHb part 
        nghb = int(np.sum(ghb_geometry))     # this is the total number of General head cells in the model
        colcell, rowcell = np.meshgrid(np.arange(0, self.ncol), np.arange(0, self.nrow))  # make mesh grid lists of all the dell indexes 
        lrchc = np.zeros((nghb, 5))       # layer(int), row(int), column(int), 
        lrchc[:, 0] = 0                                    # give it layer 1
        lrchc[:, 1] = rowcell[ghb_geometry == 1]           # assign the specific row numbers for the active ghb cells
        lrchc[:, 2] = colcell[ghb_geometry == 1]           # assign the specific col numbers for the active ghb cells
        lrchc[:, 3] = .01                                  # this is the starting head value, maybe change to 1?
        lrchc[:, 4] = 62.5                   # this is conductance values, probably change later
        # create ghb dictionary
        ghb_data = {0:lrchc}


        modelname = 'mf'

        ml = flopy.modflow.Modflow(modelname, version='mf2005', exe_name=exe_name, model_ws=mydir, verbose=False)

        discret = flopy.modflow.ModflowDis(ml, nlay=self.nlay, nrow=self.nrow, ncol=self.ncol, laycbd=0,
                                           delr=self.delr, delc=self.delc, top=top, botm=self.botm,
                                           nper=nper, perlen=perlen, nstp=nstp, tsmult=tsmult)

        bas = flopy.modflow.ModflowBas(ml, ibound=final_ibound, strt=ihead)
        lpf = flopy.modflow.ModflowLpf(ml, laytyp=laytyp, hk=HK, vka=vka)
        rch = flopy.modflow.ModflowRch(ml, rech=rch_data)
        oc = flopy.modflow.ModflowOc(ml, stress_period_data=spd)
        pcg = flopy.modflow.ModflowPcg(ml, hclose=1.0e-6, rclose=3.0e-3, mxiter=100, iter1=50)
        ghb = flopy.modflow.ModflowGhb(ml, stress_period_data=ghb_data)
        
          # water level observations
        obs_data= []
        for i in range(0,self.nobs):
            obsva = flopy.modflow.HeadObservation(ml, obsname=self.obsnames[i], 
                                                layer=self.layervals[i], row=self.rowvals[i], column=self.colvals[i],
                                                time_series_data=[[0,self.obsvals[i]]])
            obs_data.append(obsva)       
        hob = flopy.modflow.ModflowHob(ml, iuhobsv = 7, hobdry=-999, obs_data = obs_data)


        ml.write_input()
        ml.run_model(silent=False)

        observations = np.loadtxt(os.path.join(mydir, '{}.hob.out'.format(modelname)), skiprows=1, usecols=[0,1])      
        comp_obs = np.ravel(np.split(observations, 2, 1)[0]) # the computed hed values at the obspts
        obs_obs = np.ravel(np.split(observations, 2, 1)[1]) # the observed hed values at the obspts

        simul_obs = comp_obs 
        
        if self.deletedir:
            rmtree(mydir, ignore_errors=True)
            #rmtree(sim_dir)
        #return H_meas.dot(x_dummy)
        
        return simul_obs

    
    
    def run_model(self, HK, idx = 0):
        '''run adh
        '''
        simul_obs = self.run_model_single(HK,  idx)
           
        return simul_obs # 1d array

    
    def run(self, HK, par, ncores=None):
        if ncores is None:
            ncores = self.ncores

        method_args = range(HK.shape[1])
        args_map = [(HK[:, arg:arg + 1], arg) for arg in method_args]

        if par:
            pool = Pool(processes=ncores)
            simul_obs = pool.map(self, args_map)
        else:
            simul_obs = []
            for item in args_map:
                simul_obs.append(self(item))

        return np.array(simul_obs).T # make it 2D

        # pool.close()
        # pool.join()

    def __call__(self, args):
        return self.run_model(args[0], args[1])

        # return args[0](args[1], args[2])
    # return self.run_model(self,bathy,idx)
    # def run_in_parallel(self,args):
    #    return args[0].run_model(args[1], args[2])
    
    

'''    
Not sure how to code this

if __name__ == '__main__':
    import numpy as np
    #from time import time
    import mf




    # params to pass to Model class
    delr = 169 
    delc = 165
    nlay = 1
    nrow = 100
    ncol = 200
    botm = -1250

        # Pre-development water levels spreadsheet. Compiled from drillers logs and pump tests
    # monitoring well data from this  integrated framework. 
    MON_WELL_MEASUREMENT_SHEET = os.path.join("..", "..", 'Static_Data_Storage', "Ave_WL_MSL_m_mon_wells.csv")
    PREDEVELOP_WLS_2_CSV = os.path.join("..", "..", 'Static_Data_Storage', 'GIS','Predevelop_WLs_2.csv')
    Pdevel_WLs = pd.read_csv(PREDEVELOP_WLS_2_CSV)

    xll = 515244    # hard code too
    yll = 8410178

    # Just stick on the data from the measured monitoring wells (it will average both values if repeated)
    Mon_well_WLs = pd.read_csv(MON_WELL_MEASUREMENT_SHEET) 
    del Mon_well_WLs['Well_num']
    Pdevel_WLs = Pdevel_WLs.append(Mon_well_WLs, sort=False)

    Pdevel_WLs['row_num'] = Pdevel_WLs['x_utm'].apply(lambda x_utm_val: math.ceil((x_utm_val-xll)/delr) )          
    Pdevel_WLs['col_num'] = Pdevel_WLs['y_utm'].apply(lambda y_utm_val: (1+nrow)-math.ceil((y_utm_val-yll)/delc) )   
    Pdevel_WLs['rowcol']  = list(zip(Pdevel_WLs.row_num, Pdevel_WLs.col_num))                                     

    # This takes obs wells that occupy the same cell and averages them! 
    Unique_WLs = Pdevel_WLs.groupby('rowcol', as_index=False).mean()                                               

    # make new unique names for each obs point
    Unique_WLs["name"] = "Obs_"+Unique_WLs.index.map(str)

    nobs = len(Unique_WLs['WL_m_MSL']) 
    layervals = [0] * nobs
    rowvals = list(Unique_WLs['col_num'].astype(int))
    colvals = list(Unique_WLs['row_num'].astype(int))
    obsvals = list(Unique_WLs['WL_m_MSL'])
    obsnames = list(Unique_WLs["name"])

    obs_locmat = np.asarray(obsvals)
    

    mf_params = {'layervals': layervals, 'rowvals': rowvals,
              'colvals': colvals, 'obsvals':obsvals, 'obsnames':obsnames,
              'delr': delr, 'delc': delc,
              'nlay': nlay, 'nrow': nrow, 'ncol': ncol,
              'botm': botm, 'obs_locmat': obs_locmat}
    
    
    
    
    
    
    
 ###HOW DEAL WITH THIS? 

    logHK = np.loadtxt('true_logK.txt')
    logHK = np.array(logHK).reshape(-1, 1) # make it m x 1 2D array

    par = False  # parallelization false

    mymodel = Model(mf_params)
    print('1) single run')
    #logHK = np.loadtxt('shat2.txt')
    #logHK = np.array(logHK).reshape(-1, 1)
    simul_obs = mymodel.run(logHK,par)
    # generate synthetic observations
    #obs = simul_obs + 0.5*np.random.randn(simul_obs.shape[0],simul_obs.shape[1])
    #np.savetxt('obs.txt', obs)

    #print('2) parallel run with ncores = %d' % ncores)
    par = True  # parallelization false
    ncores = 2
    nrelzs = 2

    logHKrelz = np.zeros((np.size(logHK, 0), nrelzs), 'd')

    for i in range(nrelzs):
        logHKrelz[:, i:i + 1] = logHK + 0.1 * np.random.randn(np.size(logHKrelz, 0), 1)

    #simul_obs_all = mymodel.run(logHKrelz, True, ncores)

    # print(simul_obs_all)

    # use all the physcal cores if not specify ncores
    # print('3) parallel run with all the physical cores')
    # simul_obs_all = mymodel.run(logHKrelz,par)
    # print(simul_obs_all)

    simul_obs = mymodel.run(logHK,par)
'''