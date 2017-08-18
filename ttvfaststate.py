import state
import mcmc
import observations
import driver
import ttvfast
import scipy.stats
import copy

class State(object):
    def __init__(self, stel_m_planets, ttvfast_settings):
        self.stel_m_planets = stel_m_planets
        self.Time = ttvfast_settings[0]
        self.dt = ttvfast_settings[1]
        self.Total = ttvfast_settings[2]
        self.n_plan = ttvfast_settings[3]
        self.input_flags = ttvfast_settings[4]
        self.logp = None
        self.Nvars = 14+1
        
    def get_logp(self, obs):
        if (self.priorHard()):
            lnpri = -np.inf
            return lnpri
        softlnpri = 0.0
        if self.logp is None:
            self.logp = -self.get_chi2(obs)
        return self.logp + softlnpri
        
    def get_chi2(obs):
        #split and prep data for ttvfast
        for i in range(self.n_plan):
            
        planets = [:]
        stellar__mass = self.stel_m_planets[0]
        #get results...
        results = ttvfast.ttvfast(planets, stellar_mass, Time, dt, Totalx`)
        #prep results
        integer_indices, epochs, times, rsky, vsky = results["positions"]
        ttimes = times[:375]
        tinteger_indices = integer_indices[:375]
        t1_times = []
        t2_times = []
        for i in range(375):
            if(tinteger_indices[i]==0):
                t1_times.append(ttimes[i])
            else:
                t2_times.append(ttimes[i])
        #calc chi2
        chi2 = 0.
        for i in range(t1):
            chi2 += 
        return chi2


    def get_params(self):
        return self.stel_m_planets
        
    def set_params(self, stel_m_planets):
        self.stel_m_planets = stel_m_planets
    
    #Will need to modify this...
    def deepcopy(self):
        return State(copy.deepcopy(self.obs)

    def priorHard(self):
        for i in enumerate(self.stel_m_planets):
            if (self.params[2] <= 0.00001) :
                print "Invalid state was proposed (m1)"
                return True
        return False
