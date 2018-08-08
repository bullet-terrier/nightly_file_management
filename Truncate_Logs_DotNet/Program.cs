using System;
using System.Collections.Generic;
using System.Linq;
using System.IO;
using System.Text;
using System.Threading.Tasks;
using System.Configuration;

namespace Truncate_Logs_DotNet
{
    class Program
    {
        static string log_path = "./activity_log.log";
        static int maxfileage = 0;
        static FileInfo currentfile = null;

        private static float get_file_age(FileInfo alpha)
        {
            float assumed_age = 0;
            try
            {
                var a = alpha.CreationTime;
                var b = DateTime.Now;
                // how many ticks make a second?
                var c = b.Ticks - a.Ticks; //10 million ticks in a second...
                assumed_age = c / TimeSpan.TicksPerSecond;
            }
            catch
            {

            }
            return assumed_age;
        }

        static void Main(string[] args)
        {
            try
            {
                maxfileage = int.Parse(ConfigurationManager.AppSettings.GetValues("age")[0]);
            }
            catch(FormatException FE)
            {
                Console.WriteLine(FE);
                Console.WriteLine("Defaulting to 0");
            }
            catch(ArgumentNullException ANE)
            {
                Console.WriteLine(ANE);
            }
            // // could do something with the args, but not worrying about it.
            List<string> patterns = ConfigurationManager.AppSettings.GetValues("patterns").ToList<string>();
            foreach(string a in ConfigurationManager.AppSettings.GetValues("paths").ToList<string>())
            {
                if (a == "")
                {
                    continue;
                }
                try
                {
                    foreach(string b in Directory.GetFiles(a))
                    {
                        if(b=="")
                        {
                            continue;
                        }
                        currentfile = new FileInfo(b);
                        foreach(string c in patterns)
                        {
                            if (c == "")
                            {
                                continue; // this means it can exist but will be skipped.
                            }
                            if (b.Contains(c) && get_file_age(currentfile) > maxfileage && maxfileage!= 0)
                            {
                                // we won't allow a fileage of 0...
                                Console.WriteLine($"Deleting: {b}");
                                File.Delete(currentfile.FullName);
                                break;
                            }
                        }
                    }
                }
                catch(Exception e)
                {

                }
                
            }
        }

    }
}
