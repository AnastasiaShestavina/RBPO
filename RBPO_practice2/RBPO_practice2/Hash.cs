using System;
using System.Collections.Generic;
using System.Text;
using System.Security.Cryptography;

namespace RBPO_practice2
{
    internal static class Hash
    {
        internal static string GetStringHash(string password)
        {
            if (string.IsNullOrEmpty(password))
                return string.Empty;

            using (var sha = new MD5CryptoServiceProvider())
            //using (var sha = new SHA256Managed())
            {
                byte[] textData = Encoding.UTF8.GetBytes(password);
                byte[] hash = sha.ComputeHash(textData);
                return BitConverter.ToString(hash).Replace("-", string.Empty);
            }
        }
    }
}
