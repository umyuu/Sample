package com.example.umyu.sqlitesample;

import android.support.annotation.CheckResult;
import android.support.annotation.IdRes;
import android.support.annotation.NonNull;
import android.support.v7.app.AppCompatActivity;
import android.view.View;


public class BaseActivity extends AppCompatActivity {
    @NonNull
    @CheckResult
    public final View findViewById(@IdRes int id) {
        View v = super.findViewById(id);
        checkNotNull(v);
        return v;
    }
    public static <T> T checkNotNull(T reference) {
        if (reference == null) throw new NullPointerException();
        return reference;
    }
}
