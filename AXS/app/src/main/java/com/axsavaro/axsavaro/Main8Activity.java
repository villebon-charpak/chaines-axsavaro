package com.axsavaro.axsavaro;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.content.Intent;
import android.view.View;
import android.widget.ImageView;

public class Main8Activity extends AppCompatActivity {

    private ImageView retour;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main8);

        this.retour = (ImageView) findViewById(R.id.retour);

        retour.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

                Intent otherAactct = new Intent(getApplicationContext(), Main4Activity.class);
                startActivity(otherAactct);
                finish();
            }
        });
    }
}
