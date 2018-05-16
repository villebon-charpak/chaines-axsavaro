package com.axsavaro.axsavaro;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;

public class MainActivity extends AppCompatActivity {

    private ImageView compte;
    private ImageView valise;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        this.compte = (ImageView) findViewById(R.id.compte);

        compte.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent otherAct = new Intent(getApplicationContext(),Main2Activity.class);
                startActivity(otherAct);
                finish();
            }
        });

        this.valise = (ImageView) findViewById(R.id.valise);

        valise.setOnClickListener(new View.OnClickListener() {
                                      @Override
                                      public void onClick(View view) {
                                          Intent actvalise = new Intent(getApplicationContext(), Main3Activity.class);
                                          startActivity(actvalise);
                                          finish();
                                      }
    })
;}}
