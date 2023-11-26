import request from '@/utils/request'

export const getCategory = () => {
  return request({
    url: '/stock/spot',
    method: 'get'
  })
}
