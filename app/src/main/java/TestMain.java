import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.Response;

import java.io.IOException;
import java.sql.Timestamp;

public class TestMain {

    OkHttpClient client = new OkHttpClient();
    String date = "2021-04-06 1:00:00"; //Replace with your value
    Timestamp timestamp = Timestamp.valueOf(date);
    // Convert timestamp to long for use
    long timeParameter = timestamp.getTime();

    String doGetRequest(String url) throws IOException {

        Request request = new Request.Builder()
                .url("https://community-open-weather-map.p.rapidapi.com/onecall/timemachine?lat=52.21866&lon=20.99746&dt=1617757200")
                .get()
                .addHeader("x-rapidapi-key", "2f8a103f4emshe6452ebdc159a90p156155jsn9cd2567b8e5c")
                .addHeader("x-rapidapi-host", "community-open-weather-map.p.rapidapi.com")
                .build();

        Response response = client.newCall(request).execute();
        return response.body().string();
    }
    public static void main(String[] args) throws IOException {
        TestMain example = new TestMain();
        String getResponse = example.doGetRequest("https://www.vogella.com/");
        System.out.println(getResponse);
    }
}
