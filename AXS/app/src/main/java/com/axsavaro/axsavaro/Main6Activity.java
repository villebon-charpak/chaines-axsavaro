package com.axsavaro.axsavaro;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.ImageView;
import android.widget.TextView;

public class Main6Activity extends AppCompatActivity {

    private ImageView play;
    private TextView point;
    private int clicks = 0;
    private ImageView retour;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main6);


        this.point = (TextView) findViewById(R.id.point);
        this.play = (ImageView) findViewById(R.id.play);

        play.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                clicks++;
                point.setText("Points : " +clicks);

            }
        });


        this.retour = (ImageView) findViewById(R.id.retour);

        retour.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

                Intent otherAact = new Intent(getApplicationContext(), MainActivity.class);
                startActivity(otherAact);
                finish();
            }
        });

    }
}
