# BART API Wrapper for Python 3+ (w/ JSON)
Bart API Documentation: https://api.bart.gov/docs/overview/index.aspx

Every amenity from the Bay Area Rapid Transit (BART) API is implemented in some way.
The methods sections below shows the available methods. 

Each API method will return relevant data, usually with new line characters so that when
the string is printed, well-formed information is printed. The second branch of this
project, BartApiForPrintingInfo, will always print the data. 

One exception: the help class methods, which both return data and print it to screen.

Use the help class methods to see what the syntax is for invoking a bart command.

For example, the general help function:

Input

    bart = Bart()   # note that key defaults to BART API's universal key
    bart.help()
    
Output

    Commands: help, routes, routeinfo 
    route_help(), routes(), route_info()
    
    Commands: bsa, count, elev, help 
    bsa(), train_count(), elev(), elev_help()
    
    Commands: etd, help 
    etd(), etd_help()
    
    Commands: help, stns, stninfo 
    stn_help(), stninfo(), stnaccess(), stns()
    
    Commands: arrive, depart, fare, help, holiday, routesched, scheds, special, stnsched 
    arrive(), depart(), fare(), sched_help(), holiday(), routesched(), scheds(), special(), stnsched()
  
  
Also, there is thorough documentation. The following...
    
       help(classname.methodname)
       help(classname)
       
...will give you all of the necessary details about a method or class.


## Methods
    ----- Bart API -----
    bart = Bart(key)  # key is optional, defaults to universal BART API key


    Advisories
    -----------
    bsa(orig)
    train_count()
    elev()
    elev_help()


    Real-Time Estimates
    -------------------
    etd(orig, plat, direction)
    etd_help()


    Route Information
    -----------------
    routeinfo(route_num, sched_num, date)
    routes(sched_num, date)
    route_help()


    Schedule Information
    --------------------
    arrive(orig, dest time, b, a)
    depart(orig, dest, time, b, a)
    fare(orig, dest, date, sched)
    holiday()
    routesched(route, date, time, sched)
    scheds()
    special()
    stnsched(orig, date)
    sched_help()


    Station Information
    -------------------
    stn_help()
    stninfo(orig)
    stnaccess(orig)
    stns()


    Version Information
    -------------------
    version()
   
## Installing
There's a package on PyPI.

    pip3 install bart-api-ulloa

Just make sure you have python3 and the requests library (don't even need an API key, 
since BART has a universal key and it's built into this wrapper).
