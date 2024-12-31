var app = angular.module('todoApp', []);

app.controller('TodoController', function($scope, $http) {
    $scope.todos = [];
    $scope.categories = [];
    $scope.newTask = "";
    $scope.newCategory = "";
    $scope.selectedCategory = null;

    // Fetch categories
    $scope.getCategories = function() {
        $http.get('/api/categories').then(function(response) {
            $scope.categories = response.data;
        });
    };

    // Add category
    $scope.addCategory = function() {
        if ($scope.newCategory.trim() === "") return;
        $http.post('/api/categories', { name: $scope.newCategory }).then(function(response) {
            $scope.newCategory = "";
            $scope.getCategories();
        }, function(error) {
            alert(error.data.message);
        });
    };

    // Delete category
    $scope.deleteCategory = function(id) {
        $http.delete('/api/categories/' + id).then(function(response) {
            $scope.getCategories();
            $scope.getTodos();
        });
    };

    // Fetch todos
    $scope.getTodos = function() {
        $http.get('/api/todos').then(function(response) {
            $scope.todos = response.data;
        });
    };

    // Add todo
    $scope.addTodo = function() {
        if ($scope.newTask.trim() === "" || !$scope.selectedCategory) return;
        $http.post('/api/todos', { task: $scope.newTask, category_id: $scope.selectedCategory }).then(function(response) {
            $scope.newTask = "";
            $scope.getTodos();
        });
    };

    // Update todo
    $scope.updateTodo = function(todo) {
        $http.put('/api/todos/' + todo.id, { status: todo.status ? 1 : 0 }).then(function(response) {
            $scope.getTodos();
        });
    };

    // Delete todo
    $scope.deleteTodo = function(id) {
        $http.delete('/api/todos/' + id).then(function(response) {
            $scope.getTodos();
        });
    };

    // Initialize
    $scope.getCategories();
    $scope.getTodos();
});
