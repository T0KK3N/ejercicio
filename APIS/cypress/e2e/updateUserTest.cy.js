describe('Update User API Test', () => {
    it('Should update the user information', () => {
      cy.request({
        method: 'PUT',
        url: 'https://petstore.swagger.io/v2/user/danielmorademo',
        headers: {
          'Content-Type': 'application/json',
        },
        body: {
          "id": 777,
          "username": "danielmorademo",
          "firstName": "demodemodemo",
          "lastName": "Mora",
          "email": "demodemodemo@example.com",
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