using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace FaceDocVerifyClient.Modelo
{
    public  class LoginResponse
    {
        public string access_token { get; set; }
        public string token_type { get; set; }
    }
}
