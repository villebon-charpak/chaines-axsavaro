package com.axsavaro.axsavaro;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.content.Intent;
import android.view.View;
import android.widget.ImageView;

public class Main4Activity extends AppCompatActivity {

    private ImageView retour;
    private ImageView tete;
    private ImageView gorge;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main4);


        this.retour = (ImageView) findViewById(R.id.retour);

        retour.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

                Intent otherAactct = new Intent(getApplicationContext(), MainActivity.class);
                startActivity(otherAactct);
                finish();
            }
        });


        this.tete = (ImageView) findViewById(R.id.tete);
        tete.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent Acttete = new Intent (getApplicationContext(), Main5Activity.class);
                startActivity(Acttete);
                finish();
            }
        });


        this.gorge = (ImageView) findViewById(R.id.gorge);
        gorge.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent Actgorge = new Intent (getApplicationContext(), Main7Activity.class);
                startActivity(Actgorge);
                finish();
            }
        });



    }
}