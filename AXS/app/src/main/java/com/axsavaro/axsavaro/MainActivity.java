package com.axsavaro.axsavaro;

import android.content.Intent;
import android.media.MediaPlayer;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;
import android.media.MediaPlayer;


public class MainActivity extends AppCompatActivity {

    private ImageView compte;
    private ImageView valise;
    private ImageView cherche;
    private ImageView joue;

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
        });




        this.cherche = (ImageView) findViewById(R.id.cherche);

        cherche.setOnClickListener (new View.OnClickListener(){
                                    @Override
                                    public void onClick(View View){
                                        Intent actcherche = new Intent(getApplicationContext(), Main4Activity.class);
                                        startActivity(actcherche);
                                        finish();



                                    }


        });



        this.joue = (ImageView) findViewById(R.id.joue);

        joue.setOnClickListener (new View.OnClickListener(){
            @Override
            public void onClick(View View){
                Intent actjoue = new Intent(getApplicationContext(), Main6Activity.class);
                startActivity(actjoue);
                finish();



            }


        });





    }}
