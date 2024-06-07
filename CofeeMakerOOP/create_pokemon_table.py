from prettytable import PrettyTable

# Initialize the PrettyTable object
table = PrettyTable()

# Add a column to the table
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

table.align = "l"
# Print the table
print(table)
 