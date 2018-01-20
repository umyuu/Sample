package com.example.umyu.sqlitesample;

import android.content.ContentValues;
import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;
import android.database.sqlite.SQLiteDatabaseLockedException;
import android.database.sqlite.SQLiteStatement;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

import java.util.Random;

public class MainActivity extends BaseActivity {
    private SQLiteDatabase db;
    private EditText edit_text;
    private EditText edit_input;
    private EditText edit_uuid;
    private EditText edit_total;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        DBSQLiteOpenHelper helper = new DBSQLiteOpenHelper(this);
        db = helper.getReadableDatabase();
        edit_text = (EditText)findViewById(R.id.editText);
        edit_input = (EditText)findViewById(R.id.edit_input);
        edit_uuid = (EditText)findViewById(R.id.uuid);
        edit_total = (EditText)findViewById(R.id.edit_total);
        Button btn_create = (Button)findViewById(R.id.create);
        btn_create.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                insert_sql();
            }
        });
        Button btn_update = (Button)findViewById(R.id.update);
        btn_update.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                update_sql();
            }
        });
    }
    private void update_sql(){
        Long id = Long.valueOf(edit_uuid.getText().toString());
        Long d = Long.parseLong(edit_input.getText().toString());
        final String sql = "UPDATE MEMO_TABLE SET body=?,total=total+? WHERE uuid=?";

        SQLiteStatement stmt = db.compileStatement(sql);
        int row_count = 0;

            stmt.bindString(1, edit_text.getText().toString());
            stmt.bindLong(2, d);
            stmt.bindLong(3, id);
        try {
            row_count = stmt.executeUpdateDelete();
            switch(row_count) {
                case 0:
                    // 対象データなし
                    Log.e("sql", stmt.toString());
                    break;
                case 1:
                    // 正常時：更新件数が1件の時
                    Log.d("sql", String.valueOf(row_count));
                    break;
                default:
                    // 複数件（データ不整合）
                    Log.e("sql", stmt.toString());
                    break;
            }
        }finally {
            stmt.close();
        }
        select_sql();
    }
    private void select_sql(){

        Cursor cursor = db.query("MEMO_TABLE", null, "uuid=?", new String[]{edit_uuid.getText().toString()}, null, null, null, null);
        try {
            while (cursor.moveToNext()) {
                edit_text.setText(cursor.getString(cursor.getColumnIndex("body")));
                edit_total.setText(String.valueOf(cursor.getLong(cursor.getColumnIndex("total"))));
                break;
            }
        } finally {
            cursor.close();
        }
    }
    private void insert_sql(){
        Random rnd = new Random();
        final String sql = "INSERT INTO MEMO_TABLE (body,total) VALUES (?, ?)";
        SQLiteStatement stmt = db.compileStatement(sql);
        int row_count = 0;

            stmt.bindString(1, edit_text.getText().toString());
            stmt.bindLong(2, (long)rnd.nextInt(3000));
        try {
            row_count = stmt.executeUpdateDelete();
            switch(row_count) {
                case 0:
                    // 対象データなし
                    Log.e("sql", stmt.toString());
                    break;
                case 1:
                    // 正常時：更新件数が1件の時
                    Log.d("sql", String.valueOf(row_count));
                    break;
                default:
                    // 複数件（データ不整合）
                    Log.e("sql", stmt.toString());
                    break;
            }
        }finally {
            stmt.close();
        }
        select_sql();
    }
}
