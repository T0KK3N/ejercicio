describe('Create User API Test', () => {
    it('Should create a new user', () => {
      cy.request({
        method: 'POST',
        url: 'https://petstore.swagger.io/v2/user/',
        headers: {
          'Content-Type': 'application/json',
        },
        body: {
          "id": 777,
          "username": "danielmorademo",
          "firstName": "Daniel",
          "lastName": "Mora",
          "email": "danielmora@example.com",
          "password": "1234567890",
          "phone": "1234567890",
          "userStatus": 0
        }
      }).then((response) => {
        //console.log("response", response);
        expect(response.status).to.eq(200);
      });
    });
  });