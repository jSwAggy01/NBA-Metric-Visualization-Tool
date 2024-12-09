using Python.Runtime;

RunScript("tutorialScript");

static void RunScript(string scriptName)
{
    Runtime.PythonDLL = @"C:\Users\jSwAggy\AppData\Local\Programs\Python\Python311\python311.dll";
    PythonEngine.Initialize();

    using(Py.GIL())
    {
        // Add the directory containing your script to Python's search path
        dynamic sys = Py.Import("sys");
        sys.path.append(System.IO.Directory.GetCurrentDirectory());
        
        // Now try to import your script
        var pythonScript = Py.Import(scriptName);
    }
}