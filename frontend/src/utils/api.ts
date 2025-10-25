import axios from "axios";

const BASE_URL = "http://localhost:8000/api";

type json = Record<string, any>;

const e = (url: string) => {
  let split_url = url.split("?")[0];
  if (split_url.startsWith("/")) {
    split_url = split_url.substring(1);
  }
  if (!split_url.endsWith("/")) {
    split_url += "/";
  }
  const params = url.split("?")[1] ? "?" + url.split("?")[1] : "";
  return `${BASE_URL}/${split_url}${params}`;
};

const response = (data: json | json[], status: number) => {
  if (status >= 200 && status < 300) {
    return data;
  }
  return {
    error: "Server not found",
  };
};

export async function uget(endpoint: string, params?: json) {
  const { data, status } = await axios.get(e(endpoint), {
    params: params || {},
    headers: {
      Accept: "application/json",
      "Content-Type": "application/json",
    },
  });
  return response(data, status);
}

export async function upost(endpoint: string, params: json | json[]) {
  const { data, status } = await axios.post(e(endpoint), params, {
    headers: {
      Accept: "application/json",
      "Content-Type": "application/json",
    },
  });
  return response(data, status);
}

export async function get(endpoint: string, params?: json) {
  const token = localStorage.getItem("access");
  if (!token) {
    return {
      error: "Invalid Token",
    };
  }

  const { data, status } = await axios.get(e(endpoint), {
    params: params || {},
    headers: {
      Authorization: `Bearer ${token}`,
      Accept: "application/json",
      "Content-Type": "application/json",
    },
  });
  return response(data, status);
}

export async function post(endpoint: string, params?: json) {
  const token = localStorage.getItem("access");
  if (!token) {
    return {
      error: "Invalid Token",
    };
  }

  const { data, status } = await axios.psot(e(endpoint), params, {
    headers: {
      Authorization: `Bearer ${token}`,
      Accept: "application/json",
      "Content-Type": "application/json",
    },
  });
  return response(data, status);
}
