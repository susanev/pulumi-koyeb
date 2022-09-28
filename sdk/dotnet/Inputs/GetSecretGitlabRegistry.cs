// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Koyeb.Inputs
{

    public sealed class GetSecretGitlabRegistryArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The registry password
        /// </summary>
        [Input("password", required: true)]
        public string Password { get; set; } = null!;

        /// <summary>
        /// The registry username
        /// </summary>
        [Input("username", required: true)]
        public string Username { get; set; } = null!;

        public GetSecretGitlabRegistryArgs()
        {
        }
        public static new GetSecretGitlabRegistryArgs Empty => new GetSecretGitlabRegistryArgs();
    }
}
