<template>
  <v-app id="inspire">
    <navigation-and-auth></navigation-and-auth>
    <main>
      <v-content>
        <router-view></router-view>
      </v-content>
    </main>
    <v-footer color='primary' app>
      <span class="white--text">&copy; 2017. Created using VueJS and Django</span>
    </v-footer>
  </v-app>
</template>

<script>
  import NavigationAndAuth from './components/home/NavigationAndAuth'

  export default {
    components: {
      NavigationAndAuth
    }
  }
</script>
<style>
  li div a {
    text-decoration: none;
  }
</style>
