import { ZerixClient, BASE_URL, routes } from ".";

import axios from 'axios'

jest.mock('axios')

describe('Client', () => {
  let zerixClient
  beforeEach(() => {
    zerixClient = new ZerixClient('test')
  })

  test('should create a client', () => {
    expect(zerixClient).toBeDefined();
  })
  // test updateApiKey
  test('should update the api key', () => {
    zerixClient.updateApiKey('test2');
    expect(zerixClient.apiKey).toBe('test2');
  })
});

describe('Send Requests', () => {
  let zerixClient

  beforeEach(() => {
    zerixClient = new ZerixClient('test')
  })

  afterEach(() => {
    jest.resetAllMocks()
  })

  it('should make a successful request to the application parameter', async () => {
    const method = 'GET'
    const endpoint = routes.application.url
    const expectedResponse = { data: 'response' }
    axios.mockResolvedValue(expectedResponse)

    await zerixClient.sendRequest(method, endpoint)

    expect(axios).toHaveBeenCalledWith({
      method,
      url: `${BASE_URL}${endpoint}`,
      params: null,
      headers: {
        Authorization: `Bearer ${zerixClient.apiKey}`,
        'Content-Type': 'application/json',
      },
      responseType: 'json',
    })

  })

  it('should handle errors from the API', async () => {
    const method = 'GET'
    const endpoint = '/test-endpoint'
    const errorMessage = 'Request failed with status code 404'
    axios.mockRejectedValue(new Error(errorMessage))

    await expect(zerixClient.sendRequest(method, endpoint)).rejects.toThrow(
      errorMessage
    )
  })
})