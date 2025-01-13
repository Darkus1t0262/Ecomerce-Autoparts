import org.springframework.web.bind.annotation.*;
import java.sql.*;
import java.util.*;

@RestController
@RequestMapping("/analytics")
public class AnalyticsService {

    private static final String REDSHIFT_URL = "jdbc:redshift://your-cluster-url:5439/analytics";
    private static final String USERNAME = "user";
    private static final String PASSWORD = "password";

    @GetMapping("/metrics")
    public List<Map<String, Object>> getMetrics() throws SQLException {
        List<Map<String, Object>> metrics = new ArrayList<>();
        try (Connection conn = DriverManager.getConnection(REDSHIFT_URL, USERNAME, PASSWORD);
             Statement stmt = conn.createStatement();
             ResultSet rs = stmt.executeQuery("SELECT * FROM usage_metrics")) {

            while (rs.next()) {
                Map<String, Object> row = new HashMap<>();
                row.put("id", rs.getInt("id"));
                row.put("metric_name", rs.getString("metric_name"));
                row.put("value", rs.getDouble("value"));
                metrics.add(row);
            }
        }
        return metrics;
    }
}
