package com.weather;

import org.apache.commons.exec.CommandLine;
import org.apache.commons.exec.DefaultExecutor;
import org.apache.commons.exec.PumpStreamHandler;
import org.python.util.PythonInterpreter;
import org.springframework.stereotype.Controller;

import javax.script.ScriptContext;
import javax.script.ScriptEngine;
import javax.script.ScriptEngineManager;
import javax.script.SimpleScriptContext;
import java.io.*;
import java.io.InputStream;
import java.util.List;
import java.util.Scanner;

//path: E:/Kinga/Studies-mgr/Semestr 3/Praca dyplomowa/System/weather-forecast-predicting-system/print.py
@Controller
public class ScriptCaller {

    public String callScript() throws Exception {
        String data = "";
        try {
            File myObj = new File("E:/Kinga/Studies-mgr/Semestr 3/Praca dyplomowa/System/weather-forecast-predicting-system/result.txt");
            Scanner myReader = new Scanner(myObj);
            while (myReader.hasNextLine()) {
                data = myReader.nextLine();
                System.out.println(data);
            }
            myReader.close();
        } catch (FileNotFoundException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }
//        StringWriter writer = new StringWriter();
//        ScriptContext context = new SimpleScriptContext();
//        context.setWriter(writer);
//
//        ScriptEngineManager manager = new ScriptEngineManager();
//        ScriptEngine engine = manager.getEngineByName("python");
//        engine.eval(new FileReader("E:/Kinga/Studies-mgr/Semestr 3/Praca dyplomowa/System/weather-forecast-predicting-system/print.py"), context);
//        System.out.print(writer.toString().trim());
        String temp = "10";
        return data;
    }




}
