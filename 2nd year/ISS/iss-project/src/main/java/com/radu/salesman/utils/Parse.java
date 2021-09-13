package com.radu.salesman.utils;

import com.radu.salesman.ui.UIException;

public class Parse {
    public static int safeParseInteger(String toInt) throws UIException {
        try {
            return Integer.parseInt(toInt);
        } catch (NumberFormatException e) {
            throw new UIException("Please insert a valid numeric value!");
        }
    }

    public static long safeParseLong(String toLong) throws UIException {
        try {
            return Long.parseLong(toLong);
        } catch (NumberFormatException e) {
            throw new UIException("Please insert a valid numeric value!");
        }
    }

    public static float safeParseFloat(String toFloat) throws UIException {
        try {
            return Float.parseFloat(toFloat);
        } catch (NumberFormatException e) {
            throw new UIException("Please insert a valid numeric value!");
        }
    }
}