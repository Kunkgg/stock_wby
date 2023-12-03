import service from "@/utils/request";

function getStockSpot(stock_code) {
  return service({
    url: `/stock/spot/${stock_code}`,
    method: "get",
  });
}

function getStockSpotList(params) {
  return service({
    url: `/stock/spot`,
    method: "get",
    params: params,
  });
}

function refreshStockSpot() {
  return service({
    url: `/stock/spot/refresh`,
    method: "post",
  });
}

function getStockName(params) {
  return service({
    url: `/stock/name`,
    method: "get",
    params: params
  });
}

function getStockStatus() {
  return service({
    url: `/stock/status`,
    method: "get",
  });
}

export { 
  getStockSpot,
  getStockSpotList,
  refreshStockSpot,
  getStockName,
  getStockStatus
};
