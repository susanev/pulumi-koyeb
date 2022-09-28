// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Koyeb
{
    public static class GetDomain
    {
        /// <summary>
        /// {{% examples %}}
        /// ## Example Usage
        /// {{% example %}}
        /// 
        /// ```csharp
        /// using System.Collections.Generic;
        /// using Pulumi;
        /// using Koyeb = Pulumi.Koyeb;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var my_domain = Koyeb.GetDomain.Invoke(new()
        ///     {
        ///         Name = "www.exampled.tld",
        ///     });
        /// 
        /// });
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Task<GetDomainResult> InvokeAsync(GetDomainArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetDomainResult>("koyeb:index/getDomain:getDomain", args ?? new GetDomainArgs(), options.WithDefaults());

        /// <summary>
        /// {{% examples %}}
        /// ## Example Usage
        /// {{% example %}}
        /// 
        /// ```csharp
        /// using System.Collections.Generic;
        /// using Pulumi;
        /// using Koyeb = Pulumi.Koyeb;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var my_domain = Koyeb.GetDomain.Invoke(new()
        ///     {
        ///         Name = "www.exampled.tld",
        ///     });
        /// 
        /// });
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Output<GetDomainResult> Invoke(GetDomainInvokeArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetDomainResult>("koyeb:index/getDomain:getDomain", args ?? new GetDomainInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetDomainArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The app name the domain is assigned to
        /// </summary>
        [Input("appName")]
        public string? AppName { get; set; }

        /// <summary>
        /// The deployment group assigned to the domain
        /// </summary>
        [Input("deploymentGroup")]
        public string? DeploymentGroup { get; set; }

        /// <summary>
        /// The CNAME record to point the domain to
        /// </summary>
        [Input("intendedCname")]
        public string? IntendedCname { get; set; }

        /// <summary>
        /// The status messages of the domain
        /// </summary>
        [Input("messages")]
        public string? Messages { get; set; }

        /// <summary>
        /// The domain name
        /// </summary>
        [Input("name", required: true)]
        public string Name { get; set; } = null!;

        /// <summary>
        /// The date and time of when the domain was last verified
        /// </summary>
        [Input("verifiedAt")]
        public string? VerifiedAt { get; set; }

        public GetDomainArgs()
        {
        }
        public static new GetDomainArgs Empty => new GetDomainArgs();
    }

    public sealed class GetDomainInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The app name the domain is assigned to
        /// </summary>
        [Input("appName")]
        public Input<string>? AppName { get; set; }

        /// <summary>
        /// The deployment group assigned to the domain
        /// </summary>
        [Input("deploymentGroup")]
        public Input<string>? DeploymentGroup { get; set; }

        /// <summary>
        /// The CNAME record to point the domain to
        /// </summary>
        [Input("intendedCname")]
        public Input<string>? IntendedCname { get; set; }

        /// <summary>
        /// The status messages of the domain
        /// </summary>
        [Input("messages")]
        public Input<string>? Messages { get; set; }

        /// <summary>
        /// The domain name
        /// </summary>
        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        /// <summary>
        /// The date and time of when the domain was last verified
        /// </summary>
        [Input("verifiedAt")]
        public Input<string>? VerifiedAt { get; set; }

        public GetDomainInvokeArgs()
        {
        }
        public static new GetDomainInvokeArgs Empty => new GetDomainInvokeArgs();
    }


    [OutputType]
    public sealed class GetDomainResult
    {
        /// <summary>
        /// The app name the domain is assigned to
        /// </summary>
        public readonly string? AppName;
        /// <summary>
        /// The date and time of when the domain was created
        /// </summary>
        public readonly string CreatedAt;
        /// <summary>
        /// The deployment group assigned to the domain
        /// </summary>
        public readonly string DeploymentGroup;
        /// <summary>
        /// The domain ID
        /// </summary>
        public readonly string Id;
        /// <summary>
        /// The CNAME record to point the domain to
        /// </summary>
        public readonly string IntendedCname;
        /// <summary>
        /// The status messages of the domain
        /// </summary>
        public readonly string Messages;
        /// <summary>
        /// The domain name
        /// </summary>
        public readonly string Name;
        /// <summary>
        /// The organization ID owning the domain
        /// </summary>
        public readonly string OrganizationId;
        /// <summary>
        /// The status of the domain
        /// </summary>
        public readonly string Status;
        /// <summary>
        /// The domain type
        /// </summary>
        public readonly string Type;
        /// <summary>
        /// The date and time of when the domain was last updated
        /// </summary>
        public readonly string UpdatedAt;
        /// <summary>
        /// The date and time of when the domain was last verified
        /// </summary>
        public readonly string VerifiedAt;
        /// <summary>
        /// The version of the domain
        /// </summary>
        public readonly string Version;

        [OutputConstructor]
        private GetDomainResult(
            string? appName,

            string createdAt,

            string deploymentGroup,

            string id,

            string intendedCname,

            string messages,

            string name,

            string organizationId,

            string status,

            string type,

            string updatedAt,

            string verifiedAt,

            string version)
        {
            AppName = appName;
            CreatedAt = createdAt;
            DeploymentGroup = deploymentGroup;
            Id = id;
            IntendedCname = intendedCname;
            Messages = messages;
            Name = name;
            OrganizationId = organizationId;
            Status = status;
            Type = type;
            UpdatedAt = updatedAt;
            VerifiedAt = verifiedAt;
            Version = version;
        }
    }
}
