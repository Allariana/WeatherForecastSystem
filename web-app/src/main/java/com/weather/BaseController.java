package com.weather;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.servlet.ModelAndView;

import javax.servlet.http.HttpServletRequest;
import java.text.SimpleDateFormat;
import java.util.Date;

@Controller
public class BaseController {

    @RequestMapping(value = "/", method = RequestMethod.GET)
    public ModelAndView index(HttpServletRequest request) throws Exception {
        SimpleDateFormat formatter = new SimpleDateFormat("dd-MM-yyyy");
        Date date = new Date(System.currentTimeMillis());
        Date date2 = new Date(System.currentTimeMillis() + (1000 * 60 * 60 * 24));

        String today = formatter.format(date);
        String tomorrow = formatter.format(date2);

        ModelAndView model = new ModelAndView("index.html");
        model.addObject("today", today);
        model.addObject("tomorrow", tomorrow);
        return model;
    }
}
