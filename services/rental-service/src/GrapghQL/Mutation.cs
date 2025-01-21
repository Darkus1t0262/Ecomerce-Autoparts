using RentalService.Data;
using RentalService.Models;

namespace RentalService.GraphQL
{
    public class Mutation
    {
        // Add a new rental reservation
        public Rental AddRental(string vehicleName, decimal pricePerDay)
        {
            var rental = new Rental
            {
                Id = RentalData.Rentals.Count + 1,
                VehicleName = vehicleName,
                Status = "Reserved", // Newly added rentals are marked as Reserved
                PricePerDay = pricePerDay
            };

            RentalData.Rentals.Add(rental);
            return rental;
        }
    }
}
