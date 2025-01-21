namespace RentalService.Models
{
    public class Rental
    {
        public int Id { get; set; }
        public string VehicleName { get; set; }
        public string Status { get; set; } // e.g., "Available", "Reserved"
        public decimal PricePerDay { get; set; }
    }
}
