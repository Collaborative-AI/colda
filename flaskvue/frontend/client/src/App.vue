<template>
  <div id="app">
    <div id="nav">
      <router-link to="/">Home</router-link> |
      <router-link to="/about">About</router-link> |
      <router-link to="/ping">Ping</router-link> |
      <router-link to="/ceshi">Ceshi</router-link> |
      <router-link to="/books">Books</router-link>
    </div>
    <router-view/>
  </div>
</template>

<style>
#app {
  margin-top: 60px;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
