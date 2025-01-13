import com.amazonaws.services.dynamodbv2.AmazonDynamoDB;
import com.amazonaws.services.dynamodbv2.AmazonDynamoDBClientBuilder;
import com.amazonaws.services.dynamodbv2.document.DynamoDB;
import com.amazonaws.services.dynamodbv2.document.Item;
import com.amazonaws.services.dynamodbv2.document.Table;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/inventory")
public class InventoryService {
    private final AmazonDynamoDB client = AmazonDynamoDBClientBuilder.defaultClient();
    private final DynamoDB dynamoDB = new DynamoDB(client);
    private final Table table = dynamoDB.getTable("inventory");

    @GetMapping
    public List<Item> getAllInventory() {
        return table.scan().getItems();
    }

    @PostMapping
    public String updateInventory(@RequestBody Map<String, Object> payload) {
        table.putItem(new Item().withPrimaryKey("id", payload.get("id")).withMap("data", payload));
        return "Inventory updated successfully!";
    }
}
