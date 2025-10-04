const normalizeBaseUrl = (value) => {
  if (!value) {
    return '';
  }
  const trimmed = value.trim();
  if (!trimmed) {
    return '';
  }
  return trimmed.endsWith('/') ? trimmed.slice(0, -1) : trimmed;
};

const DEFAULT_BASE = '/api';

const configuredBase = normalizeBaseUrl(import.meta.env.VITE_API_BASE_URL);
const baseUrl = configuredBase || normalizeBaseUrl(DEFAULT_BASE);

const buildUrl = (path) => {
  if (!path) {
    return baseUrl;
  }
  const normalizedPath = path.startsWith('/') ? path : `/${path}`;
  if (!baseUrl) {
    return normalizedPath;
  }
  return `${baseUrl}${normalizedPath}`;
};

export const apiUrl = (path = '') => {
  if (/^https?:\/\//i.test(path)) {
    return path;
  }
  return buildUrl(path);
};

export const apiFetch = (path, options = {}) => {
  const url = apiUrl(path);
  return fetch(url, options);
};

export const API_BASE_URL = baseUrl || '/';
