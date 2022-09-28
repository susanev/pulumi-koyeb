// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Koyeb
{
    /// <summary>
    /// ## Example Usage
    /// 
    /// ```csharp
    /// using System.Collections.Generic;
    /// using Pulumi;
    /// using Koyeb = Pulumi.Koyeb;
    /// 
    /// return await Deployment.RunAsync(() =&gt; 
    /// {
    ///     var my_app = new Koyeb.KoyebApp("my-app");
    /// 
    /// });
    /// ```
    /// </summary>
    [KoyebResourceType("koyeb:index/koyebApp:KoyebApp")]
    public partial class KoyebApp : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The date and time of when the app was created
        /// </summary>
        [Output("createdAt")]
        public Output<string> CreatedAt { get; private set; } = null!;

        /// <summary>
        /// The app domains
        /// </summary>
        [Output("domains")]
        public Output<ImmutableArray<Outputs.KoyebAppDomain>> Domains { get; private set; } = null!;

        /// <summary>
        /// The app name
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// The organization ID owning the app
        /// </summary>
        [Output("organizationId")]
        public Output<string> OrganizationId { get; private set; } = null!;

        /// <summary>
        /// The date and time of when the app was last updated
        /// </summary>
        [Output("updatedAt")]
        public Output<string> UpdatedAt { get; private set; } = null!;


        /// <summary>
        /// Create a KoyebApp resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public KoyebApp(string name, KoyebAppArgs? args = null, CustomResourceOptions? options = null)
            : base("koyeb:index/koyebApp:KoyebApp", name, args ?? new KoyebAppArgs(), MakeResourceOptions(options, ""))
        {
        }

        private KoyebApp(string name, Input<string> id, KoyebAppState? state = null, CustomResourceOptions? options = null)
            : base("koyeb:index/koyebApp:KoyebApp", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                PluginDownloadURL = "https://github.com/koyeb/pulumi-koyeb/releases/download/v${VERSION}",
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing KoyebApp resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static KoyebApp Get(string name, Input<string> id, KoyebAppState? state = null, CustomResourceOptions? options = null)
        {
            return new KoyebApp(name, id, state, options);
        }
    }

    public sealed class KoyebAppArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The app name
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        public KoyebAppArgs()
        {
        }
        public static new KoyebAppArgs Empty => new KoyebAppArgs();
    }

    public sealed class KoyebAppState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The date and time of when the app was created
        /// </summary>
        [Input("createdAt")]
        public Input<string>? CreatedAt { get; set; }

        [Input("domains")]
        private InputList<Inputs.KoyebAppDomainGetArgs>? _domains;

        /// <summary>
        /// The app domains
        /// </summary>
        public InputList<Inputs.KoyebAppDomainGetArgs> Domains
        {
            get => _domains ?? (_domains = new InputList<Inputs.KoyebAppDomainGetArgs>());
            set => _domains = value;
        }

        /// <summary>
        /// The app name
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The organization ID owning the app
        /// </summary>
        [Input("organizationId")]
        public Input<string>? OrganizationId { get; set; }

        /// <summary>
        /// The date and time of when the app was last updated
        /// </summary>
        [Input("updatedAt")]
        public Input<string>? UpdatedAt { get; set; }

        public KoyebAppState()
        {
        }
        public static new KoyebAppState Empty => new KoyebAppState();
    }
}
