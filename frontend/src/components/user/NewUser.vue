<template lang="html">
  <v-dialog v-model="dialog" persistent max-width="500px">
    <v-btn color="orange" dark slot="activator">New User</v-btn>
    <v-card>
      <v-form v-model="valid" ref="form" lazy-validation>
        <v-card-title>
          <span class="headline">Please Enter Credentials</span>
        </v-card-title>
        <v-card-text>
          <v-container grid-list-md>
            <v-layout wrap>
              <v-flex xs12>
                <v-text-field
                 label="Username"
                 v-model="username"
                 required
                ></v-text-field>
              </v-flex>
              <v-flex xs12>
                <v-text-field
                  label="Password"
                  type="password"
                  v-model="password"
                  :rules="passwordRules"
                  required
                ></v-text-field>
              </v-flex>
              <v-flex xs12>
                <v-text-field
                  label="Password Again"
                  type="password"
                  v-model="password_dup"
                  :rules="passwordRules"
                  required
                ></v-text-field>
              </v-flex>
            </v-layout>
          </v-container>
          <small>*indicates required field</small>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="red" @click.native="dialog = false; clear()">Close</v-btn>
          <v-btn color="green" @click.native="create()">Create</v-btn>
        </v-card-actions>
      </v-form>
    </v-card>
  </v-dialog>
</template>

<script>
import axios from 'axios'

export default {
  data: function () {
    return {
      dialog: false,
      valid: false,
      username: '',
      password: '',
      passwordRules: [
        (v) => !!v || 'Password is required',
        (v) => (v && v.length <= 5) || 'Company name must be greater than 5 characters'
      ],
      password_dup: ''
    }
  },
  methods: {
    login: function () {
      if (this.$refs.form.validate()) {
        var formData = new FormData()
        formData.append('username', this.username)
        formData.append('password', this.password)

        axios.post('/user/login', formData)
          .then(response => {
            this.dialog = false
            this.clear()
          })
          .catch(e => {
            console.log("Couldn't Create New User In!")
          })
      }
    },
    clear: function () {
      this.$refs.form.reset()
    }
  }
}
</script>

<style lang="css">
</style>
