<!-- Navbar admin -->
<template>
  <nav class="bg-sky-600 text-white p-4 flex justify-between items-center">
    <div class="space-x-4">
      <router-link to="/admin/contestants" class="hover:underline">Concursantes</router-link>
      <router-link to="/admin/winner" class="hover:underline">Ganador</router-link>
    </div>
    <button @click="logout" class="bg-red-500 px-3 py-1 rounded hover:bg-red-600">Cerrar sesión</button>
  </nav>
</template>

<script lang="ts">
import { useRouter } from "vue-router";

export default {
  setup() {
    const router = useRouter();

    const logout = () => {
      localStorage.removeItem("adminToken");
      router.push("/admin/login");
    };

    return { logout };
  },
};
</script>
