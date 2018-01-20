package com.example.umyu.sqlitesample;

import android.content.Context;
import android.database.sqlite.SQLiteDatabase;
import android.database.sqlite.SQLiteOpenHelper;

public class DBSQLiteOpenHelper extends SQLiteOpenHelper {
    private Context context;
    private static final String DB_NAME = "sqlite_demo.db";
    private static final int DB_VERSION = 1;
    public DBSQLiteOpenHelper(final Context context) {
        super(context, DB_NAME, null, DB_VERSION);
        this.context = context;
    }
    @Override
    public void onCreate(SQLiteDatabase db) {
        db.execSQL("create table MEMO_TABLE(" +
                        " 'uuid' INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE," +
                        " 'body' TEXT DEFAULT ''," +
                        " 'total' INTEGER DEFAULT 0" +
                        ")");
    }
    @Override
    public void onUpgrade (SQLiteDatabase db, int oldVersion, int newVersion) {

    }

    @Override
    public void onDowngrade (SQLiteDatabase db, int oldVersion, int newVersion) {

    }
}
