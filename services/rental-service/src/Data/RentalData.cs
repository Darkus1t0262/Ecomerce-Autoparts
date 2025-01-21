using System.Collections.Generic;
using RentalService.Models;

namespace RentalService.Data
{
    public static class RentalData
    {
        public static List<Rental> Rentals = new List<Rental>
        {
            new Rental { Id = 1, VehicleName = "Toyota Corolla", Status = "Available", PricePerDay = 45.50m },
            new Rental { Id = 2, VehicleName = "Ford Explorer", Status = "Reserved", PricePerDay = 70.00m },
            new Rental { Id = 3, VehicleName = "Honda Civic", Status = "Available", PricePerDay = 50.00m },
        };
    }
}
