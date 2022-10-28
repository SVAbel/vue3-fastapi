<template>
  <div>
    <div class="card">
      <h5>Hello, data-developer</h5>
      <TabMenu :model="items" />
    </div>
  </div>
</template>

<script>
// import Login from "../comps/Login.vue";
// import UserAccount from '../comps/UserAccount.vue';
import TabMenu from 'primevue/tabmenu';
import { ref } from 'vue';

export default {
  setup() {
    const active = ref(3);
    const items = ref([
      {
        label: 'Home',
        icon: 'pi pi-fw pi-home',
        to: '/',
      },
      {
        label: 'Calendar',
        icon: 'pi pi-fw pi-calendar',
        to: '/calendar',
      },
      {
        label: 'Edit',
        icon: 'pi pi-fw pi-pencil',
        to: '/edit',
      },
      {
        label: 'Documentation',
        icon: 'pi pi-fw pi-file',
        to: '/documentation',
      },
      {
        label: 'Settings',
        icon: 'pi pi-fw pi-cog',
        to: '/settings',
      },
    ]);

    return { active, items };
  },
  components: {
    // Login,
    // UserAccount,
    TabMenu,
  },
  data() {},
  methods: {
    isLoggedIn() {
      return this.$store.state.auth.status.loggedIn;
    },
  },
};
</script>
<style scoped lang="scss">
::v-deep(.tabmenudemo-content) {
  padding: 2rem 1rem;
}
</style>
