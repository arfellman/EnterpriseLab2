# EnterpriseLab2

* Examine the code snippets provided and port (refactor) the code into Python 3.x compatible runtime.
* Develop a basic test case for each to ensure the ported code is accurate.
* Create a process flow diagram for each application you port.



Test Code in C# .NET:

using System;
using System.Collections.Generic;
using System.Linq;

namespace csharp_sample
{
    class Program
    {
        static void Main(string[] args)
        {
            List<int> someNumbersList = new List<int>();
            //double myaverage = someNumbersList.Average();
            for (int i = 0; i <3; i++)
            {
            Console.WriteLine("Enter your a number:");
            int someNum = Convert.ToInt32(Console.ReadLine());
            someNumbersList.Add(someNum);
            }
            Console.WriteLine("The average is: {0}", someNumbersList.Average());
        }
    }
}




Test code in PowerShell:

Import-Module -Name RestPS
<#
The JSON payload in the file looks like this. With RestPS you have to use a file.
[
  {
    "RequestType": "GET",
    "RequestURL": "/",
    "RequestCommand": "Get-Date -ErrorAction SilentlyContinue"
  }
]

The output of Get-Date looks like this: "Monday, August 23, 2021 8:32:17 PM"
For more examples see: https://github.com/jpsider/RestPS/blob/master/RestPS/endpoints/RestPSRoutes.json
#>

Start-RestPSListener -Port 8000 -RoutesFilePath ./jsonroute.json