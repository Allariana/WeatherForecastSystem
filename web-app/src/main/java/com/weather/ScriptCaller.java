package com.weather;

import javax.annotation.PostConstruct;
import javax.script.*;

import org.junit.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;
import java.io.FileReader;
import java.io.StringWriter;
import org.springframework.stereotype.Controller;

@Controller
public class ScriptCaller {

    public String callScript() throws Exception {

//        StringWriter writer = new StringWriter(); //ouput will be stored here
//
//        ScriptEngineManager manager = new ScriptEngineManager();
//        ScriptContext context = new SimpleScriptContext();
//
//        context.setWriter(writer); //configures output redirection
//        ScriptEngine engine = manager.getEngineByName("python");
//        engine.eval(new FileReader("E:/Kinga/Studies-mgr/Semestr 3/Praca dyplomowa/System/weather-forecast-predicting-system/actual_weather_prediction.py"), context);
//        System.out.println(writer.toString());
//        String temp = writer.toString();
        String temp = "10";
        return temp;
    }




}
