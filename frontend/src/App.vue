<template>
  <!-- <nav>
    <router-link to="/">Home</router-link> |
    <router-link to="/about">About</router-link> |
    <router-link to="/bom">bom</router-link> |
    <router-link to="/calendar">calendar</router-link> |
    <router-link to="/counsel">counsel</router-link> |
    <router-link to="/dashboard">dashboard</router-link> |
    <router-link to="/login">login</router-link> |
    <router-link to="/payment">payment</router-link> |
    <router-link to="/reception">reception</router-link>
  </nav> -->
  <router-view />
</template>

<script>
export default {
  name: 'App',
  components: {},
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
