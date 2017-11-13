import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    debug: true,
    expiration: 0,
    time: Date.now()
  },
  mutations: {
    SET_AUTH: function (state, expiration) {
      state.expiration = expiration
      console.log(Date.now())
      console.log(expiration)
    },
    REMOVE_AUTH: function (state) {
      state.expiration = 0
    },
    SET_TIME: function (state, time) {
      state.time = time
    }
  },
  actions: {
    setAuth: function ({commit}, expiration) {
      commit('SET_AUTH', expiration)
    },
    removeAuth: function ({commit}) {
      commit('REMOVE_AUTH')
    },
    setTime: function ({commit}) {
      commit('SET_TIME', Date.now())
    }
  },
  getters: {
    expiration: state => state.expiration,
    time: state => state.time,
    expired: state => state.expiration < state.time,
    timeLeft: state => state.expiration - state.time
  }
})
