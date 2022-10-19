using System;
using System.Collections.Generic;
using System.IO;
using System.Text;
using System.Text.RegularExpressions;

namespace RBPO_practice2
{
    internal static class Menu
    {
        internal static void ThreadChoiceShow()
        {

            Console.WriteLine("Выберете режим:");
            Console.WriteLine("1. Работа в однопоточном режиме");
            Console.WriteLine("2. Работа в многопоточном режиме");
            string choice = Console.ReadLine();

            switch (choice)
            {
                case "1":
                    string hash = HashEnter();
                    SingleThread.BruteHash(hash.ToUpper());
                    break;
                case "2":
                    hash = HashEnter();
                    MultiThreading.BruteHash(hash.ToUpper());
                    break;
            }
        }

        private static string HashEnter()
        {
            Console.WriteLine("Введите хэш");
            string hash = Console.ReadLine();

            if (Regex.IsMatch(hash, @"^[A-Za-z0-9]*$"))
                return hash;
            else
            {
                Console.WriteLine("Хэш может содержать только цифры и буквы от A до F в любом регистре");
                return "error";
            }
        }
    }
}
