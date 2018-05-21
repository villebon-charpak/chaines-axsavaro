package com.axsavaro.axsavaro;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.ImageView;
import android.content.Intent;


public class Main7Activity extends AppCompatActivity {
    private ImageView retour;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main7);

        this.retour = (ImageView) findViewById(R.id.retour);
        retour.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent actretour = new Intent(getApplicationContext(), MainActivity.class);
                startActivity (actretour);
                finish();
            }
        });




    }
}
