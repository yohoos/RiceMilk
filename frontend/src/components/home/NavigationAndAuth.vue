<template>
  <div>
    <v-navigation-drawer clipped persistent light :mini-variant.sync="mini" v-model="drawer" enable-resize-watcher app>
      <v-toolbar flat class="transparent">
        <v-list class="pa-0">
          <v-list-tile avatar>
            <v-list-tile-avatar>
              <img
                src="https://avatars2.githubusercontent.com/u/12375128?v=4&s=400&u=44411691244718d092661e0dc4e4a9704c6b5365"/>
            </v-list-tile-avatar>
            <v-list-tile-content>
              <v-list-tile-title>Yuhua Ni</v-list-tile-title>
            </v-list-tile-content>
            <v-list-tile-action>
              <v-btn icon @click.native.stop="mini = !mini">
                <v-icon>chevron_left</v-icon>
              </v-btn>
            </v-list-tile-action>
          </v-list-tile>
        </v-list>
      </v-toolbar>
      <v-list class="pt-0" dense>
        <v-divider></v-divider>
        <v-list-tile v-for="route in routes.slice(0,1)" :key="route.name" @click="goTo (route)">
          <v-list-tile-action>
            <v-icon>{{ route.icon }}</v-icon>
          </v-list-tile-action>
          <v-list-tile-content>
            <v-list-tile-title>{{ route.name }}</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>
        <v-list-tile>
          <v-list-tile-content>
            <v-list-tile-title>Projects</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>
        <v-list-tile v-for="route in routes.slice(1)" :key="route.name" @click="goTo (route)">
          <v-list-tile-action>
            <v-icon>{{ route.icon }}</v-icon>
          </v-list-tile-action>
          <v-list-tile-content>
            <v-list-tile-title>{{ route.name }}</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>
      </v-list>
    </v-navigation-drawer>
    <v-toolbar color='primary' clipped-left dark fixed app>
      <v-toolbar-side-icon @click.stop="drawer = !drawer"></v-toolbar-side-icon>
      <v-toolbar-title>Welcome</v-toolbar-title>
      <v-spacer></v-spacer>
      <div v-if="!authenticated">
        <new-user></new-user>
        <login></login>
      </div>
      <div v-if="authenticated">
        <logout></logout>
      </div>
      <alerts></alerts>
    </v-toolbar>
  </div>
</template>

<script>
  import Login from '../user/Login'
  import NewUser from '../user/NewUser'
  import Logout from '../user/Logout'
  import Alerts from '../user/Alerts'
  import axios from 'axios'

  export default {
    components: {
      Login,
      NewUser,
      Logout,
      Alerts
    },
    data: () => ({
      drawer: true,
      routes: [],
      mini: false,
      right: null
    }),
    props: {
      source: String
    },
    methods: {
      goTo: function (route) {
        if (route.html === true) {
          window.location.replace(route.path)
        } else {
          this.$router.push({
            name: route.name,
            params: {}
          })
        }
      },
      setTime: function () {
        this.$store.dispatch('setTime')
      },
      checkAuthentication: function () {
        axios.get('/user_auth/api_auth_check')
          .then(response => {
            var data = response.data
            if (data['authenticated'] === true) {
              this.$store.dispatch('setAuth', data['expires'])
              console.log('Is Authenticated')
            } else {
              console.log('Not Authenticated!')
            }
          })
          .catch(error => {
            console.log(error)
          })
      }
    },
    created: function () {
      this.$router.options.routes.forEach(route => {
        this.routes.push(route)
      })

      this.checkAuthentication()
      setInterval(this.setTime, 1000)
    },
    computed: {
      authenticated: function () {
        return !this.$store.getters.expired
      }
    }
  }
</script>
