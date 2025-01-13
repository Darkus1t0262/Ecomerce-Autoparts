import org.springframework.web.bind.annotation.*;
import org.apache.tinkerpop.gremlin.driver.Cluster;
import org.apache.tinkerpop.gremlin.driver.Client;
import java.util.*;

@RestController
@RequestMapping("/recommendations")
public class RecommendationService {

    private final Cluster cluster;
    private final Client client;

    public RecommendationService() {
        cluster = Cluster.build("neptune-endpoint").create();
        client = cluster.connect();
    }

    @GetMapping("/{productId}")
    public List<Map<String, Object>> getRecommendations(@PathVariable String productId) {
        String query = String.format("g.V('%s').out('related_to').valueMap(true)", productId);
        List<Map<String, Object>> recommendations = new ArrayList<>();
        client.submit(query).stream().forEach(result -> recommendations.add(result.getObject()));
        return recommendations;
    }
}
