package com.weather;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.servlet.ModelAndView;

import javax.servlet.http.HttpServletRequest;

@Controller
public class BaseController extends ScriptCaller{

    @RequestMapping(value = "/", method = RequestMethod.GET)
    public ModelAndView index(HttpServletRequest request) throws Exception {
        String temp = callScript();
        ModelAndView model = new ModelAndView("index.html");
        model.addObject("temp", temp);
        return model;
    }
}
