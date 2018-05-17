package sh.surge.idp_groep12.idp_app;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        update();
    }

    public void update(){
        TextView t = (TextView) findViewById(R.id.label);
        t.setText("label test!");
        TextView t2 = (TextView) findViewById(R.id.info);
        t2.setText("info test");
    }
}
