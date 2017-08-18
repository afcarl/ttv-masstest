import state
import mcmc
import observations
import driver
import ttvfast
import scipy.stats
import copy

class TTVState(object):
    def __init__(self, stel_m_planets, ttvfast_settings):
        self.stel_m_planets = stel_m_planets
        self.ttvfast_settings = ttvfast_settings
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
        
    def get_chi2(self, obs):
        #split and prep data for ttvfast
        params = self.stel_m_planets
        planet1 = ttvfast.models.Planet(*params[1:1 + 7])
        planet2 = ttvfast.models.Planet(*params[1 + 7:])
        stellar_mass = params[0]
        planets = [planet1, planet2]            
        #get results...
        results = ttvfast.ttvfast(planets, stellar_mass, self.Time, self.dt, self.Total)
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
        fac = len(t1_times)
        for i in range(len(t1_times)):
            chi2 += (t1_times[i] - obs.times[i])**2. * 1./(obs.errors[i])**2. * fac
        return chi2

    def get_params(self):
        return self.stel_m_planets
        
    def set_params(self, stel_m_planets):
        self.stel_m_planets = stel_m_planets
    
    #Will need to modify this...
    def deepcopy(self):
        return TTVState(copy.deepcopy(self.stel_m_planets), copy.deepcopy(self.ttvfast_settings))

    def priorHard(self):
        for i in enumerate(self.stel_m_planets):
            if (self.stel_m_planets[2] <= 0.00001) :
                print "Invalid state was proposed (m1)"
                return True
        return False

