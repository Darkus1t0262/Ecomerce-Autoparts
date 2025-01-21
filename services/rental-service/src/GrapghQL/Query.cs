using HotChocolate;
using RentalService.Data;
using RentalService.Models;
using System.Linq;

namespace RentalService.GraphQL
{
    public class Query
    {
        // Get all rentals
        public IQueryable<Rental> GetRentals() => RentalData.Rentals.AsQueryable();

        // Get a specific rental by ID
        public Rental GetRental(int id) => RentalData.Rentals.FirstOrDefault(r => r.Id == id);
    }
}
