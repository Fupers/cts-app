import { defineStore } from "pinia";
import api from "@/services/api";

export const useContestantStore = defineStore("contestant", {
  state: () => ({
    contestants: [] as any[],
    total: 0,
    next: null,
    previous: null,
    loading: false,
    error: null as string | null,
  }),

  actions: {
    // Registro publico
    async register(data: { name: string; email: string; phone: string }) {
      try {
        this.loading = true;
        const res = await api.post("/contest/register/", data);
        return res.data;
      } catch (err: any) {
        this.error = err.response?.data?.error || "Error en registro";
        throw err;
      } finally {
        this.loading = false;
      }
    },

    // Verificación publica con token
    async verify(token: string) {
      try {
        this.loading = true;
        const res = await api.post("/contest/verify/", { token });
        return res.data;
      } catch (err: any) {
        this.error = err.response?.data?.error || "Error en verificación";
        throw err;
      } finally {
        this.loading = false;
      }
    },

    // Obtener concursantes (requiere admin token)
    async fetchContestants(page = 1) {
      try {
        this.loading = true;

        const token = localStorage.getItem("adminToken");
        if (!token) {
          window.location.href = "/admin/login";
          return;
        }

        const res = await api.get("admin/contest/", {
          params: { page },
          headers: { Authorization: `Bearer ${token}` },
        });

        this.contestants = res.data.results;
        this.total = res.data.count;
        this.next = res.data.next;
        this.previous = res.data.previous;
      } catch (err: any) {
        this.error = err.response?.data?.detail || err.message;

        if (err.response?.status === 401) {
          localStorage.removeItem("adminToken");
          window.location.href = "/admin/login";
        }
      } finally {
        this.loading = false;
      }
    },
  },
});
