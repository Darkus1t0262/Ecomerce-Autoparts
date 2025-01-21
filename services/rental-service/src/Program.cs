using Microsoft.AspNetCore.Builder;
using Microsoft.Extensions.DependencyInjection;
using RentalService.GraphQL;

var builder = WebApplication.CreateBuilder(args);

// Add HotChocolate GraphQL services
builder.Services
    .AddGraphQLServer()
    .AddQueryType<Query>()       // Register Query type
    .AddMutationType<Mutation>(); // Register Mutation type

var app = builder.Build();

// Map GraphQL endpoint
app.MapGraphQL();

app.Run();
