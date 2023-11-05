document.addEventListener('DOMContentLoaded', function () {
    const ingredientInput = document.getElementById('ingredientInput');
    const searchButton = document.getElementById('searchButton');
    const recipeList = document.getElementById('recipeList');
    const recipeForm = document.getElementById('recipeForm');

    // Sample data for demonstration
    const recipes = [
        {
            name: 'Spaghetti Carbonara',
            ingredients: 'Spaghetti, Eggs, Pancetta, Parmesan Cheese, Black Pepper',
            instructions: '1. Cook spaghetti. 2. Fry pancetta. 3. Beat eggs and cheese. 4. Combine all ingredients.'
        },
        {
            name: 'Caesar Salad',
            ingredients: 'Romaine Lettuce, Croutons, Parmesan Cheese, Caesar Dressing',
            instructions: '1. Toss lettuce and croutons. 2. Add cheese and dressing. 3. Mix well.'
        }
    ];

    // Function to display search results
    function displayRecipes(results) {
        recipeList.innerHTML = '';
        for (const recipe of results) {
            const listItem = document.createElement('li');
            listItem.textContent = recipe.name;
            recipeList.appendChild(listItem);
        }
    }

    // Search for recipes based on entered ingredients
    searchButton.addEventListener('click', function () {
        const query = ingredientInput.value.toLowerCase();
        const results = recipes.filter(recipe =>
            recipe.ingredients.toLowerCase().includes(query)
        );
        displayRecipes(results);
    });

    // Add a new recipe
    recipeForm.addEventListener('submit', function (e) {
        e.preventDefault();
        const name = document.getElementById('recipeName').value;
        const ingredients = document.getElementById('ingredients').value;
        const instructions = document.getElementById('instructions').value;
        recipes.push({ name, ingredients, instructions });
        recipeForm.reset();
        displayRecipes(recipes);
    });

    // Display sample recipes on page load
    displayRecipes(recipes);
});
