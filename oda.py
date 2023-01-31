from odafunction import LocalPythonFunction
from odafunction.func.urifunc import URIPythonFunction, URIipynbFunction    
import odafunction.logs
from fcat import Cat       

odafunction.logs.app_logging.setup()    

__all__ = ["fd", "fc", "results"]


fd = Cat(asdict=True)  


fc = Cat()

fc.add("cites", 
        URIPythonFunction("file:///home/savchenk/grb221009/cite_semantic.py::gen"))


results = fc.grbbase(focus_obs_name="total_3p")['data']

eventrate = fd.eventrate
# print("results", results)

